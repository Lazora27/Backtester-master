import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
