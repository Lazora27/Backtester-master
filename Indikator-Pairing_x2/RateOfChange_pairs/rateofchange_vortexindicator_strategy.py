import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'VortexIndicator': 1.0
        })
    )
