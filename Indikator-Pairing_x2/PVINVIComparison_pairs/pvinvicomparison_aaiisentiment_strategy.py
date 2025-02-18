import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AAIISentiment': 1.0
        })
    )
