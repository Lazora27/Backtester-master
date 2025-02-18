import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
