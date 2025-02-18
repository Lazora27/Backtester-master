import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und FisherTransform
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'FisherTransform': 1.0
        })
    )
