import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
