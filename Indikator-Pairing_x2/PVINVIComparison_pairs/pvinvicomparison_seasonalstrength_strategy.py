import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'SeasonalStrength': 1.0
        })
    )
