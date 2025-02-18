import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'UlcerIndex': 1.0
        })
    )
