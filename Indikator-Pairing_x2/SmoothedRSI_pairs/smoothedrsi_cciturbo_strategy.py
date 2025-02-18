import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und CCITurbo
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'CCITurbo': 1.0
        })
    )
