import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'MACDPredictor': 1.0
        })
    )
