import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und GannAngles
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'GannAngles': 1.0
        })
    )
