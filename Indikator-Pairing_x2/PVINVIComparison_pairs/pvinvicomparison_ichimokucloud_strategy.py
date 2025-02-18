import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'IchimokuCloud': 1.0
        })
    )
