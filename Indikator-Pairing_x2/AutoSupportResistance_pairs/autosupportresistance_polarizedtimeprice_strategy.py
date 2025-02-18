import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
