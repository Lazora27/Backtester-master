import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und FisherSignals
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'FisherSignals': 1.0
        })
    )
