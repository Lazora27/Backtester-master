import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
