import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'AverageTrueRange': 1.0
        })
    )
