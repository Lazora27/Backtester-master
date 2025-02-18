import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'CCITurbo': 1.0
        })
    )
