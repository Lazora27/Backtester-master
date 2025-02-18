import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und MassIndex
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'MassIndex': 1.0
        })
    )
