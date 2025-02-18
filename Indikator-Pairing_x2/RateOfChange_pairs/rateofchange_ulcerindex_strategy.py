import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'UlcerIndex': 1.0
        })
    )
