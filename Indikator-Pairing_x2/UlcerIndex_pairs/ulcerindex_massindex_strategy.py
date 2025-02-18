import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'MassIndex': 1.0
        })
    )
