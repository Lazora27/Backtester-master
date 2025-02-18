import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
