import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
