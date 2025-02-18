import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'PVINVIComparison': 1.0
        })
    )
