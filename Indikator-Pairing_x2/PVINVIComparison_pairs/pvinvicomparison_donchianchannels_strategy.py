import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'DonchianChannels': 1.0
        })
    )
