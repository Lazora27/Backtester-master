import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
