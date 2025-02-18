import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und FisherSignals
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'FisherSignals': 1.0
        })
    )
