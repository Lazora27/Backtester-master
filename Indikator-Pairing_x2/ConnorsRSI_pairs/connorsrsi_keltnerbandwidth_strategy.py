import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
