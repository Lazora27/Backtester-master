import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und CCITurbo
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'CCITurbo': 1.0
        })
    )
