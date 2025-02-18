import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'DonchianVolatility': 1.0
        })
    )
