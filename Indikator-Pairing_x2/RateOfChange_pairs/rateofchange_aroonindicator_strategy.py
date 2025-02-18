import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'AroonIndicator': 1.0
        })
    )
