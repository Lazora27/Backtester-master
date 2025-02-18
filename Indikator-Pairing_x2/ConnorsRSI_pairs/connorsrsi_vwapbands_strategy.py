import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und VWAPBands
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'VWAPBands': 1.0
        })
    )
