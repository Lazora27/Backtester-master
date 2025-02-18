import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
