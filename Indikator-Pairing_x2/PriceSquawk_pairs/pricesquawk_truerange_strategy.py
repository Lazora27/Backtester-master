import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und TrueRange
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'TrueRange': 1.0
        })
    )
