import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'PriceSquawk': 1.0
        })
    )
