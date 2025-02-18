import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
