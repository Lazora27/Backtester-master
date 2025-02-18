import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'VortexIndicator': 1.0
        })
    )
