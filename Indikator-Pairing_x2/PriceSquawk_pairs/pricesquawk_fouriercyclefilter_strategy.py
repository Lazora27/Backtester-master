import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
