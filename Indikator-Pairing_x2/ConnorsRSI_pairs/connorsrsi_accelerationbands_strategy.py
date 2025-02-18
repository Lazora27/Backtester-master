import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'AccelerationBands': 1.0
        })
    )
