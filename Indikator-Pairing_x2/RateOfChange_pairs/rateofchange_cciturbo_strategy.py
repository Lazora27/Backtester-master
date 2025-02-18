import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und CCITurbo
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'CCITurbo': 1.0
        })
    )
