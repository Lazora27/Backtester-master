import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und CCITurbo
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'CCITurbo': 1.0
        })
    )
