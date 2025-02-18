import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und CCITurbo
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'CCITurbo': 1.0
        })
    )
