import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
