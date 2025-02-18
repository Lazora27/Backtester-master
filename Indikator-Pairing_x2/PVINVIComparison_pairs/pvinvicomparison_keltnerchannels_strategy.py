import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'KeltnerChannels': 1.0
        })
    )
