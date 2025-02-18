import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PriceSquawk': 1.0
        })
    )
