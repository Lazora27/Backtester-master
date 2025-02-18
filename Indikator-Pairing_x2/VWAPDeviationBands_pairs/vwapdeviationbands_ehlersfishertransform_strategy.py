import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
