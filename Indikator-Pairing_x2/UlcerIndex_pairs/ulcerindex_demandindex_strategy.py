import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und DemandIndex
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'DemandIndex': 1.0
        })
    )
