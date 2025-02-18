import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinAccumulationIndex_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinAccumulationIndex und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ChaikinAccumulationIndex': {
                'class': ChaikinAccumulationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinAccumulationIndex'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ChaikinAccumulationIndex': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
