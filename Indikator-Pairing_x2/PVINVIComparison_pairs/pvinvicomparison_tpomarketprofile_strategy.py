import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
