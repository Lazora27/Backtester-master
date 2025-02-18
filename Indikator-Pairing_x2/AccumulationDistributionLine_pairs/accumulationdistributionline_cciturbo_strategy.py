import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'CCITurbo': 1.0
        })
    )
