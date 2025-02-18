import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und GannFans
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'GannFans': 1.0
        })
    )
