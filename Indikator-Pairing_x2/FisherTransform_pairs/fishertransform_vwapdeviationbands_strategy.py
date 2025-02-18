import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
