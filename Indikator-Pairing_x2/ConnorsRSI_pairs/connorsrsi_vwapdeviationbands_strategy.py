import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
