import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und FisherSignals
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'FisherSignals': 1.0
        })
    )
