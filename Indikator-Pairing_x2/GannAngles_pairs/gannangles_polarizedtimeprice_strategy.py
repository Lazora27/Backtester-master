import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
