import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
